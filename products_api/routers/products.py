from fastapi import APIRouter, status

router = APIRouter()


@router.get('/', status_code=status.HTTP_200_OK)
async def list_products():
    return {
        'products': [
            {
                'id': 1,
                'name': 'Logitech MX Keys',
            },
            {
                'id': 2,
                'name': 'RTX 5070',
            },
            {
                'id': 3,
                'name': 'SSD 1TB',
            },
        ]
    }
