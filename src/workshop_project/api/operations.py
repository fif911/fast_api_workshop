"""
Обработчик
"""
from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import Response

from workshop_project import tables, models
from workshop_project.database import get_session
from workshop_project.models.auth import User
from workshop_project.models.operations import Operation, OperationKind, OperationCreate, OperationUpdate
from workshop_project.services.auth import get_current_user
from workshop_project.services.operations import OperationService

router = APIRouter(
    prefix='/operations',
    tags=['operations'],

)


# Depends for dependency injection
@router.get('/', response_model=List[Operation])
# def get_operations(session: Session = Depends(get_session)):  # we are not calling this func we passing it into Depend
def get_operations(
        kind: Optional[OperationKind] = None,  # looks in request body - nothing, looks in url pattern - nothing - then
        # it's parameter in query string
        user: User = Depends(get_current_user),
        service: OperationService = Depends()
):
    """
    Get operations list for current user

    - **kind**: filter by
    \f everything that is followed by \f fast will ignore
    :param kind:
    :param user:
    :param service:
    :return:
    """
    return service.get_list(user_id=user.id, kind=kind)

    # operations = (
    #     session.query(tables.Operation).all()
    # )
    # return operations

    # it's bad approach cause all the time we need to open and close session
    # session = Session() # from workshop_project.database import Session
    # operations = (
    #     session.query(tables.Operation).all()
    # )
    # session.close()


@router.post('/', response_model=Operation)
def create_operation(
        operation_data: OperationCreate,
        user: User = Depends(get_current_user),
        service: OperationService = Depends()
):
    return service.create(user.id, operation_data)


@router.get('/{operation_id}', response_model=Operation)
def get_operation(
        operation_id: int,
        user: User = Depends(get_current_user),
        service: OperationService = Depends(),
):
    return service.get(user.id, operation_id)


@router.put('/{operation_id}', response_model=Operation)
def update_operation(
        operation_id: int,
        operation_data: OperationUpdate,
        user: User = Depends(get_current_user),
        service: OperationService = Depends(),
):
    return service.update(user.id,
                          operation_id, operation_data
                          )


@router.delete('/{operation_id}', response_model=Operation)
def operation_delete(
        operation_id: int,
        user: User = Depends(get_current_user),
        service: OperationService = Depends(),
):
    service.delete(user.id, operation_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
