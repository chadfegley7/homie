from system.core.router import routes

routes['default_controller'] = 'Users'
routes['POST']['/register'] = 'Users#register'
routes['POST']['/login'] = 'Users#login'
routes['GET']['/success'] = 'Users#success'
routes['GET']['/profile'] = 'Users#profile'
routes['GET']['/friends_page'] = 'Users#friends_page'
routes['GET']['/messages_page'] = 'Users#messages_page'
routes['GET']['/communicate'] = 'Users#communicate'
routes['GET']['/register_page'] = 'Users#register_page'
routes['GET']['/logout'] = 'Users#logout'

routes['POST']['/about_me'] = 'Users#about_me'
routes['POST']['/location'] = 'Users#location'

routes['GET']['/about'] = 'Users#about'
routes['GET']['/contact'] = 'Users#contact'



routes['POST']['/post_message'] = 'Messages#post_message'

routes['GET']['/process_home'] = 'Matches#process_home'
routes['GET']['/home/<friend_id>'] = 'Matches#home'
routes['POST']['/home/<friend_id>'] = 'Matches#process_match'


routes['POST']['/process_login'] = 'Users#process_login'

