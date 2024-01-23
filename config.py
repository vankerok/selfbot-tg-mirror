# -*- coding: utf8 -*-

from_channel = {
    1111111111: '#examplechannel',            # forward from channel ( id ): "name that will be used during parsing"
}

to_channel = 1111111111                       # mirror to, channel or forum ( id )
forum_topic = 1111                            # mirror to specific topic ( id ) - only if you want to parse to forum thread, otherwise just delete this line

tg_user = {
    'name': '',                               # api name        https://my.telegram.org/
    'api_id': '',                             # api id          https://my.telegram.org/
    'api_hash': ''                            # api hash        https://my.telegram.org/
}
