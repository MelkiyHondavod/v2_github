

def heal( s ):
    replace_dict = {
        "{'":'{"',
        "':":'":',
        " '":' "',
        "None":"null",
        "True":"true",
        "False":"false",
        "',":'",',
        "'}":'"}',
        "<":'"<', #optional
        ">":'>"', #optional
        '"':"\\\""# works?
    }

    for r_key in replace_dict.keys() :
        output_str = ""
        c=0
        while c<len(s):
            if   s[c] == r_key[0]  and  r_key == s[c:c+len(r_key):]  :
                output_str += replace_dict[ r_key ]
                c += len(r_key)

            else:
                output_str += s[c]
                c+=1  

        s = output_str


    return output_str            



def test():
    test_input = """{'update_id': 754941234, 'message': None, 'edited_message': None, 'channel_post': None, 'edited_channel_post': None, 'inline_query': None, 'chosen_inline_result': None, 'callback_query': {'id': '4000683675744759175', 'from_user': <telebot.types.User object at 0x0000015542A65270>, 'message': <telebot.types.Message object at 0x0000015542A65F00>, 'inline_message_id': None, 'chat_instance': '4854591940504344813', 'data': 'new_search', 'game_short_name': None, 'json': {'id': '4000683675744759175', 'from': {'id': 931481755, 'is_bot': False, 'first_name': 'чел', 'last_name': 'просто чел', 'username': 'bubylba1251', 'language_code': 'ru'}, 'message': {'message_id': 57, 'from': {'id': 6378927209, 'is_bot': True, 'first_name': 'avassist', 'username': 'avassist_fake_bot'}, 'chat': {'id': 931481755, 'first_name': 'чел', 'last_name': 'просто чел', 'username': 'bubylba1251', 'type': 'private'}, 'date': 1690750605, 'text': 'выберите желаемое действие в меню', 'reply_markup': {'inline_keyboard': [[{'text': 'новый поиск', 'callback_data': 'new_search'}]]}}, 'chat_instance': '4854591940504344813', 'data': 'new_search'}}, 'shipping_query': None, 'pre_checkout_query': None, 'poll': None, 'poll_answer': None, 'my_chat_member': None, 'chat_member': None, 'chat_join_request': None}"""
    print( heal( test_input ) )


def main():
    test()

if __name__ == "__main__" :
    main()               