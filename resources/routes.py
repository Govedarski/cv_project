from resources.user.auth_resources import RegisterUserResource, LoginUserResource

routes = (
    (RegisterUserResource, "/users/register"),  # POST
    (LoginUserResource, "/users/login"),  # POST
    # (LoginUserViaGoogleResource, "/users/customers/login/google"),  # POST
    # (AuthorizeUserViaGoogleResource, "/users/customers/authorize/google"),  # POST    #
    # (WebhookResource, "/webhook")
)

