from app.database.models import User, Category, Product, async_session
from sqlalchemy import select


async def get_categories():
    async with async_session() as session:
        result = await session.scalars(select(Category))
        return result


async def get_products(category_id):
    async with async_session() as session:
        result = await session.scalars(select(Product).where(Product.category_id == category_id))
        return result



async def get_product(product_id) -> Product:
    async with async_session() as session:
        result = await session.scalar(select(Product).where(Product.id == product_id))
        return result
