"""Reflecting Purchase table changes

Revision ID: 71deeb345cf3
Revises: d5d5898f0e15
Create Date: 2024-04-07 12:15:35.793117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71deeb345cf3'
down_revision = 'd5d5898f0e15'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('purchases', schema=None) as batch_op:
        batch_op.add_column(sa.Column('address', sa.String(length=250), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('purchases', schema=None) as batch_op:
        batch_op.drop_column('address')

    # ### end Alembic commands ###