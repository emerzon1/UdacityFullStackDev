"""empty message

Revision ID: 80d891fb3cfe
Revises: fe458085f48d
Create Date: 2019-12-02 23:25:00.698715

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80d891fb3cfe'
down_revision = 'fe458085f48d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'artists', ['name'])
    op.create_unique_constraint(None, 'venues', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'venues', type_='unique')
    op.drop_constraint(None, 'artists', type_='unique')
    # ### end Alembic commands ###