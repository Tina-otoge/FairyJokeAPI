"""game release datetime to date1

Revision ID: 39ab6bebb0b1
Revises: 643edf0bf441
Create Date: 2021-04-15 03:21:45.100260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39ab6bebb0b1'
down_revision = '643edf0bf441'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('release', schema=None) as batch_op:
        batch_op.drop_column('start_date')
        batch_op.drop_column('end_date')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('release', schema=None) as batch_op:
        batch_op.add_column(sa.Column('end_date', sa.DATETIME(), nullable=True))
        batch_op.add_column(sa.Column('start_date', sa.DATETIME(), nullable=True))

    # ### end Alembic commands ###
