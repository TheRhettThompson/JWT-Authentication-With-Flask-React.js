"""empty message

Revision ID: 9a5f9666fab6
Revises: 76a0c64a61c4
Create Date: 2023-01-06 23:22:08.569951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a5f9666fab6'
down_revision = '76a0c64a61c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vehicles', schema=None) as batch_op:
        batch_op.drop_constraint('vehicles_classification_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vehicles', schema=None) as batch_op:
        batch_op.create_unique_constraint('vehicles_classification_key', ['classification'])

    # ### end Alembic commands ###
