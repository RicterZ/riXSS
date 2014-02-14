

urls = (
    '/', 'IndexHandler',
    '/([\d]+)', 'XSScriptHandler',
    '/users', 'RedirectHandler',
    '/users/([\d]+)', 'UserHandler',
    '/modules/([\d]+)/delete', 'DelModuleHandler',
    '/projects/([\d]+)/delete', 'ProjectHandler',
    '/projects/([\d]+)/edit', 'ProjectHandler',
    '/projects/([\d]+)/results', 'XSSResultHandler',
    '/projects/([\d]+)/results/clean', 'XSSResultCleanHandler',
    '/projects/([\d]+)/results/([\d]+)/delete', 'XSSResultDelHandler',
    '/xss', 'XSSHandler',
    '/modules', 'ModuleHandler',
    '/login', 'LoginHandler',
    '/reg', 'RegHandler',
    '/logout', 'LogoutHandler',
)