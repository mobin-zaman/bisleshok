"""empty message

Revision ID: 3c3bf983a181
Revises: 
Create Date: 2019-11-28 22:33:32.027804

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c3bf983a181'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('topic',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('index_id', sa.Integer(), nullable=True),
    sa.Column('roman_index', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['index_id'], ['index.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('sub_topic',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('request_string', sa.String(length=200), nullable=False),
    sa.Column('topic_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['topic_id'], ['topic.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sub_topic')
    op.drop_table('topic')
    # ### end Alembic commands ###
