"""Edited WorkExpModel

Revision ID: 935d7bb96c3a
Revises: 9c15a99a1c24
Create Date: 2023-04-14 17:37:03.325712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '935d7bb96c3a'
down_revision = '9c15a99a1c24'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('work_exp', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('work_exp', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=500),
               nullable=False)

    # ### end Alembic commands ###
