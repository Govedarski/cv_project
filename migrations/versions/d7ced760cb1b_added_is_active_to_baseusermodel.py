"""Added is_active to BaseUserModel

Revision ID: d7ced760cb1b
Revises: 722b92d9ea63
Create Date: 2023-02-27 19:44:07.632276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7ced760cb1b'
down_revision = '722b92d9ea63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###
