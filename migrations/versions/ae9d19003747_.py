"""empty message

Revision ID: ae9d19003747
Revises: 3d3c1a9f5962
Create Date: 2023-01-05 00:50:55.790161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae9d19003747'
down_revision = '3d3c1a9f5962'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('diameter', sa.Integer(), nullable=False),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.Column('climate', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('climate'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    # ### end Alembic commands ###
