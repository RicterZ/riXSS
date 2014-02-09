

urls = (
    '/', 'IndexHandler',
    '/([\d]+)', 'XSScriptHandler',
    '/users', 'UserHandler',
    '/modules/([\d]+)/delete', 'DelModuleHandler',
    '/projects/([\d]+)/delete', 'DelProjectHandler',
    '/xss', 'XSSHandler',
    '/results/([\d]+)', 'XSSResultHandler',
    '/modules', 'ModuleHandler',
    '/login', 'LoginHandler',
    '/reg', 'RegHandler',
    '/logout', 'LogoutHandler',
)