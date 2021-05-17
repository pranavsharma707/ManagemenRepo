from fastapi import APIRouter,status
from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from models import Organization,Tenant,Role,TenantUser
import models
from settings import get_db
from schema import User ,userRole
import uuid
def id_uuids():
    uid=uuid.uuid4()
    id_uid=str(uid)
    print(type(id_uid))
    return id_uid
router=APIRouter()

@router.post('/role/',status_code=status.HTTP_200_OK)
def create_role(request:userRole, db: Session = Depends(get_db)):
    id_uid = id_uuids()
    role = Role(id=id_uid, name=request.name)
    db.add(role)
    db.commit()
    db.refresh(role)
    return role




@router.post('/userRegisteration/',status_code=status.HTTP_201_CREATED)
def userRegisteration(request:User,db:Session=Depends(get_db)):

    id_uid=id_uuids()
    organization=Organization(id=id_uid,name=request.organization_name)
    db.add(organization)
    db.commit()
    db.refresh(organization)

    id_uid = id_uuids()
    tenant=Tenant(id=id_uid,name=request.tenant_name, organization_id=organization.id)
    db.add(tenant)
    db.commit()
    db.refresh(tenant)

    role = db.query(models.Role).filter(models.Role.name == "admin").first()
    if role:
        role_id=role.id

    else:

        role_id = Role(id=id_uid, name="tenentAdmin")
        db.add(role_id)
        db.commit()
        db.refresh(role_id)
        print(role_id)

    tenantuser = TenantUser(id=id_uid, username=request.username,
                        first_name=request.firstname,
                        last_name=request.lastname, email=request.email, role_id=role_id,
                        tenant_id=tenant.id)
    db.add(tenantuser)
    db.commit()
    db.refresh(tenantuser)

    return {organization,tenant,tenantuser}


@router.get('/getdata/{id}')
def getData(id:str,db:Session=Depends(get_db)):
    data=id
    print(id)
    user=db.query(Organization).filter(Organization.id==id).first()
    terrant=db.query(Tenant).filter(Tenant.organization_id==data).first()
    terrant_user=db.query(TenantUser).filter(TenantUser.tenant_id==data).first()
    return (user,terrant,terrant_user)



