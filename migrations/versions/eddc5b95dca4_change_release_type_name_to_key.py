"""change release type name to key

Revision ID: eddc5b95dca4
Revises: 5e9b365483be
Create Date: 2021-04-15 03:30:10.329717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eddc5b95dca4'
down_revision = '5e9b365483be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('release_type', schema=None) as batch_op:
        batch_op.add_column(sa.Column('key', sa.String(), nullable=True))
        batch_op.create_unique_constraint(batch_op.f('uq_release_type_key'), ['key'])
        batch_op.drop_column('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('release_type', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.VARCHAR(), nullable=True))
        batch_op.drop_constraint(batch_op.f('uq_release_type_key'), type_='unique')
        batch_op.drop_column('key')

    # ### end Alembic commands ###
