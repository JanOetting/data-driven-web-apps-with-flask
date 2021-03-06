"""Added last updated field

Revision ID: b1b588677b3c
Revises: 
Create Date: 2020-05-02 22:16:37.631535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1b588677b3c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('packages', sa.Column('updated_date', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_packages_updated_date'), 'packages', ['updated_date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_packages_updated_date'), table_name='packages')
    op.drop_column('packages', 'updated_date')
    # ### end Alembic commands ###
