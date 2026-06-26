from fastapi import APIRouter, Depends, status

from sqlalchemy.ext.asyncio import AsyncSession

from products_api.core.database import get_session
from products_api.models.products import Product

from products_api.schemas.products import (
    ProductListPublicSchema,
    ProductPublicSchema,
    ProductSchema
)

router = APIRouter()

@router.post(
        path='/',
        status_code=status.HTTP_201_CREATED,
        response_model=ProductPublicSchema,
        summary='Criar novo produto',
)

async def create_product(
    product: ProductSchema,
    db: AsyncSession = Depends(get_session),

):
    db_product = Product(
        name=product.name,
        price=product.price,
        description=product.description,
    )

    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)

    return db_product


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
