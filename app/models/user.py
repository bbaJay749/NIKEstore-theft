from sqlalchemy import String, Column, Boolean
#from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):
    user_id = Column(String(20), primary_key=True, index=True)
    pwd = Column(String(256), nullable=True)
    first_name = Column(String(256), nullable=True)
    last_name = Column(String(256), nullable=True)
    email = Column(String, index=True, nullable=False)
    is_superuser = Column(Boolean, default=False)
    
    # wish_list는 relationship으로 연결 필요함
    wish_list = Column(String(256), nullable=True)
    '''recipes = relationship(
        "Recipe",
        cascade="all,delete-orphan",
        back_populates="submitter",
        uselist=True,
    )
    '''
