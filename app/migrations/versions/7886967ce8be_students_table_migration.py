"""Students table migration

Revision ID: 7886967ce8be
Revises: 
Create Date: 2024-03-29 14:00:22.864096

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7886967ce8be'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student')
    # ### end Alembic commands ###
