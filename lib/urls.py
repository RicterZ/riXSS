

urls = (
    '/', 'IndexHandler',
    '/([\d]+)', 'XSScriptHandler',
    #I prefer `[\d\w]+` todo
    '/user', 'UserHandler',
    '/delete/module/([\d]+)', 'DelModuleHandler',
    '/delete/project/([\d]+)', 'DelProjectHandler',
    '/xss', 'XSSHandler',
    '/result/([\d]+)', 'XSSResultHandler',
    '/login', 'LoginHandler',
    '/reg', 'RegHandler',
    '/logout', 'LogoutHandler',
)