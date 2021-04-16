"""release release_type_id -> type_id

Revision ID: a527e604e095
Revises: eddc5b95dca4
Create Date: 2021-04-16 20:23:46.767978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a527e604e095'
down_revision = 'eddc5b95dca4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('release', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('fk_release_release_type_id_release_type', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_release_type_id_release_type'), 'release_type', ['type_id'], ['id'])
        batch_op.drop_column('release_type_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('release', schema=None) as batch_op:
        batch_op.add_column(sa.Column('release_type_id', sa.INTEGER(), nullable=True))
        batch_op.drop_constraint(batch_op.f('fk_release_type_id_release_type'), type_='foreignkey')
        batch_op.create_foreign_key('fk_release_release_type_id_release_type', 'release_type', ['release_type_id'], ['id'])
        batch_op.drop_column('type_id')

    # ### end Alembic commands ###
