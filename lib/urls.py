

urls = (
    '/', 'IndexHandler',
    '/([\d]+)', 'XSScriptHandler',
    '/users', 'UserHandler',
    '/modules/([\d]+)/delete', 'DelModuleHandler',
    '/projects/([\d]+)/delete', 'ProjectHandler',
    '/projects/([\d]+)/edit', 'ProjectHandler',
    '/xss', 'XSSHandler',
    '/results/([\d]+)', 'XSSResultHandler',
    '/modules', 'ModuleHandler',
    '/login', 'LoginHandler',
    '/reg', 'RegHandler',
    '/logout', 'LogoutHandler',
)