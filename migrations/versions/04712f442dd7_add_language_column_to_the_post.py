"""add language column to the post

Revision ID: 04712f442dd7
Revises: 3356cd7b9be0
Create Date: 2024-04-02 18:06:45.368554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04712f442dd7'
down_revision = '3356cd7b9be0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('language', sa.String(length=5), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('language')

    # ### end Alembic commands ###
