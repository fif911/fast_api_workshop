from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from workshop_project.models.auth import UserCreate, Token, User
from workshop_project.services.auth import AuthService, get_current_user

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)


@router.post('/sign-up', response_model=Token)
def sign_up(user_data: UserCreate, service: AuthService = Depends()):
    return service.register_new_user(user_data)


@router.post(
    '/sign-in/',
    response_model=Token,
)
def sign_in(
        auth_data: OAuth2PasswordRequestForm = Depends(),
        auth_service: AuthService = Depends(),
):
    return auth_service.authenticate_user(
        auth_data.username,
        auth_data.password,
    )


@router.get(
    '/user/',
    response_model=User,
)
def get_user(user: User = Depends(get_current_user)):
    return user
