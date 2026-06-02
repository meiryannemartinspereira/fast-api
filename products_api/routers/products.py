from fastapi import APIRouter, status

from products_api.schemas.products import ProductListPublicSchema

router = APIRouter()


@router.get(
    path='/',
    status_code=status.HTTP_200_OK,
    response_model=ProductListPublicSchema,
)
async def list_products():
    return {
        'products': [
            {
                'id': 1,
                'name': 'Logitech MX Keys',
                'price': 729.90,
                'description': 'Bom!',
            },
            {
                'id': 2,
                'name': 'RTX 5070',
                'price': 1290.90,
                'description': 'Bom!',
            },
            {
                'id': 3,
                'name': 'SSD 1TB',
                'price': 429.90,
                'description': 'Bom!',
            },
        ]
    }
