from domain.order_status import OrderStatus
from repository.order_repository import OrderRepository
from .exceptions import ShippedOrdersCannotBeChangedException, \
    RejectedOrderCannotBeApprovedException, ApprovedOrderCannotBeRejectedException
from .order_approval_request import OrderApprovalRequest


class OrderApprovalUseCase:
    def __init__(self, order_repository: OrderRepository) -> None:
        self._order_repository = order_repository

    def run(self, request: OrderApprovalRequest) -> None:
        order = self._order_repository.get_by_id(request.order_id)
        if request.approved:
            order.approve()
        else:
            order.reject()
        self._order_repository.save(order)
