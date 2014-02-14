

urls = (
    '/', 'IndexHandler',
    '/([\d]+)', 'XSScriptHandler',
    '/users', 'RedirectHandler',
    '/users/([\d]+)', 'UserHandler',
    '/modules', 'ModulesHandler',
    '/modules/([\d]+)', 'ModuleHandler',
    '/modules/([\d]+)/delete', 'DelModuleHandler',
    '/projects/([\d]+)/delete', 'ProjectHandler',
    '/projects/([\d]+)/edit', 'ProjectHandler',
    '/projects/([\d]+)/results', 'XSSResultHandler',
    '/projects/([\d]+)/results/clean', 'XSSResultCleanHandler',
    '/projects/([\d]+)/results/([\d]+)/delete', 'XSSResultDelHandler',
    '/xss', 'XSSHandler',
    '/reg', 'RegHandler',
    '/login', 'LoginHandler',
    '/logout', 'LogoutHandler',
)