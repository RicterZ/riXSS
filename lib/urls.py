

urls = (
    '/', 'IndexHandler',
    '/([\d]+)', 'XSScriptHandler',
    '/users', 'UserHandler',
    '/modules/([\d]+)/delete', 'DelModuleHandler',
    '/projects/([\d]+)/delete', 'ProjectHandler',
    '/projects/([\d]+)/edit', 'ProjectHandler',
    '/projects/([\d]+)/results', 'XSSResultHandler',
    '/xss', 'XSSHandler',
    '/modules', 'ModuleHandler',
    '/login', 'LoginHandler',
    '/reg', 'RegHandler',
    '/logout', 'LogoutHandler',
)