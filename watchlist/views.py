
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.shortcuts import render

from .models import Watch


UserModel = get_user_model()


def watch(request, content_type, obj_id):
    """
    Adds item to watch list.
    """
    ctype = ContentType.objects.get(id=content_type)
    obj = ctype.get_object_for_this_type(pk=obj_id)

    # see if we have a logged in user and we can get that user
    watchlist = "watchlist: "
    if request.user.is_authenticated():
        if len(Watch.objects.filter(
                subscriber=request.user,
                content_type=ctype.id,
                object_id=obj_id)) == 0:
            watchitem = Watch(subscriber=request.user, content_type=ctype, object_id=obj_id)
            watchitem.save()
    else:  # no logged in user, so check session for watching, and add object
        if 'watchlist' not in request.session:
            request.session['watchlist'] = {}
        watchlist = request.session['watchlist']
        key = ctype.app_label + '|' + content_type

        # if the type is already in watchlist, append
        if key in watchlist:
            if obj_id not in watchlist[key]:
                watchlist[key].append(obj_id)
        # otherwise, create
        else:
            watchlist[key] = [obj_id]
        request.session.modified = True

    if request.is_ajax():
        return HttpResponse(watchlist, mimetype="text/html")
    return render(request, 'watchlist/watch_item_added.html', {'obj': obj})


def unwatch(request, content_type, obj_id):
    """ Removes watched item from watch list. """
    ctype = ContentType.objects.get(model=content_type)
    try:
        watchItem = Watch.objects.get(
            subscriber=request.user,
            content_type=ctype.id,
            object_id=obj_id
        )
        watchItem.delete()
    except:
        try:
            watchlist = request.session['watchlist'][ctype.name]
            watchlist.remove(int(obj_id))
            request.session.modified = True
        except:
            pass

    if request.is_ajax():
        return HttpResponse('Removed', mimetype="text/html")
    return render(request, 'watchlist/watch_item_removed.html', {'obj': 'deleted'})


def watchlist(request, slug=''):
    """ Returns list of all watched items. """
    watch_items = []
    from_session = False
    try:
        if slug:
            user = UserModel.objects.get(username=slug)
        else:
            user = UserModel.objects.get(id=request.user.id)
        watch_items = Watch.objects.filter(subscriber=user)
    except:
        if 'watchlist' in request.session:
            watch_cookie_dict = request.session['watchlist']
            watch_items = {}
            for key, v in watch_cookie_dict.items():
                key = key.split('|')
                ctype = ContentType.objects.get(app_label=key[0], model=key[1])
                watching = ctype.model_class().objects.filter(id__in=v)
                watch_items[key[1]] = watching
                from_session = True
    return render(request, 'watchlist/watch_list.html', {
        'watch_list': watch_items,
        'from_session': from_session,
    })
