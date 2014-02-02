

urls = (
    '/', 'IndexHandler',
    '/([\d]+)', 'XSScriptHandler',
    #I prefer `[\d\w]+` todo
    '/user/([\d]+)', 'UserHandler',
    '/xss', 'XSSHandler',
    '/result/([\d]+)', 'XSSResultHandler',
    '/login', 'LoginHandler',
    '/reg', 'RegHandler',
    '/logout', 'LogoutHandler',
)