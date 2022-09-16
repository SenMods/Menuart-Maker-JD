import os, struct, zlib


    # making directories
    

print('Menuart Generator for Just Dance 2015+')
codename=input('MapCode: ')
codenamelow=codename.lower()
os.makedirs(codename, exist_ok=True)
os.makedirs(codename+'/cache/itf_cooked/pc/world/maps/'+codenamelow+'/menuart')
os.makedirs(codename+'/cache/itf_cooked/pc/world/maps/'+codenamelow+'/menuart/actors', exist_ok=True)
os.makedirs(codename+'/cache/itf_cooked/pc/world/maps/'+codenamelow+'/menuart/textures/', exist_ok=True)
os.makedirs(codename+'/cache/itf_cooked/pc/world/maps/'+codenamelow+'/timeline/pictos', exist_ok=True)
os.makedirs(codename+'/cache/itf_cooked/pc/world/maps/'+codenamelow+'/videoscoach', exist_ok=True)
os.makedirs(codename+'/world/maps/'+codenamelow+'/timeline/moves/pcu/', exist_ok=True)
os.makedirs(codename+'/world/maps/'+codenamelow+'/videoscoach', exist_ok=True)
os.makedirs(codename+'/world/maps/'+codenamelow+'autodance', exist_ok=True)
menuartpath='world/maps/'+codenamelow+'/menuart/textures/'
generictganame=codenamelow+'_cover_generic.tga'
onlinetganame=codenamelow+'_cover_online.tga'
albumbkgtganame=codenamelow+'_cover_albumbkg.tga'
albumcoachtganame=codenamelow+'_cover_albumcoach.tga'
bannertganame=codenamelow+'_banner_bkg.tga'
coach1tganame=codenamelow+'_coach_1.tga'
coach2tganame=codenamelow+'_coach_2.tga'
coach3tganame=codenamelow+'_coach_3.tga'
coach4tganame=codenamelow+'_coach_4.tga'

genericname=codename+'_cover_generic'
onlinename=codename+'_cover_online'
albumbkgname=codename+'_cover_albumbkg'
albumcoachname=codename+'_cover_albumcoach'
coach1name=codename+'_coach_1'
coach2name=codename+'_coach_2'
coach3name=codename+'_coach_3'
coach4name=codename+'_coach_4'

coach=b'\x00\x00\x00\x01\x00\x00\x00\x00\x3F\x80\x00\x00\x3F\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x22\x74\x70\x6C\x5F\x6D\x61\x74\x65\x72\x69\x61\x6C\x67\x72\x61\x70\x68\x69\x63\x63\x6F\x6D\x70\x6F\x6E\x65\x6E\x74\x32\x64\x2E\x74\x70\x6C\x00\x00\x00\x1A\x65\x6E\x67\x69\x6E\x65\x64\x61\x74\x61\x2F\x61\x63\x74\x6F\x72\x74\x65\x6D\x70\x6C\x61\x74\x65\x73\x2F\xB4\xA8\x17\xA8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x72\xB6\x1F\xC5\x3F\x80\x00\x00\x3F\x80\x00\x00\x3F\x80\x00\x00\x3F\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00'
menuartbottom1=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x17\x6D\x75\x6C\x74\x69\x74\x65\x78\x74\x75\x72\x65\x5F\x31\x6C\x61\x79\x65\x72\x2E\x6D\x73\x68\x00\x00\x00\x18\x77\x6F\x72\x6C\x64\x2F\x5F\x63\x6F\x6D\x6D\x6F\x6E\x2F\x6D\x61\x74\x73\x68\x61\x64\x65\x72\x2F\xD7\xE7\xD9\xC7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3F\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'
menuartbottom2=b'\xA8\x10\x5B\x4D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x17\x6D\x75\x6C\x74\x69\x74\x65\x78\x74\x75\x72\x65\x5F\x31\x6C\x61\x79\x65\x72\x2E\x6D\x73\x68\x00\x00\x00\x18\x77\x6F\x72\x6C\x64\x2F\x5F\x63\x6F\x6D\x6D\x6F\x6E\x2F\x6D\x61\x74\x73\x68\x61\x64\x65\x72\x2F\xD7\xE7\xD9\xC7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3F\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'
menuartbottom3=b'\x2F\xB1\x51\x63\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x17\x6D\x75\x6C\x74\x69\x74\x65\x78\x74\x75\x72\x65\x5F\x31\x6C\x61\x79\x65\x72\x2E\x6D\x73\x68\x00\x00\x00\x18\x77\x6F\x72\x6C\x64\x2F\x5F\x63\x6F\x6D\x6D\x6F\x6E\x2F\x6D\x61\x74\x73\x68\x61\x64\x65\x72\x2F\xD7\xE7\xD9\xC7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3F\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'
menuartbottom4=b'\x04\xA3\x53\x23\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x17\x6D\x75\x6C\x74\x69\x74\x65\x78\x74\x75\x72\x65\x5F\x31\x6C\x61\x79\x65\x72\x2E\x6D\x73\x68\x00\x00\x00\x18\x77\x6F\x72\x6C\x64\x2F\x5F\x63\x6F\x6D\x6D\x6F\x6E\x2F\x6D\x61\x74\x73\x68\x61\x64\x65\x72\x2F\xD7\xE7\xD9\xC7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3F\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'
menuartbottom5=b'\x9C\xD9\x44\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x17\x6D\x75\x6C\x74\x69\x74\x65\x78\x74\x75\x72\x65\x5F\x31\x6C\x61\x79\x65\x72\x2E\x6D\x73\x68\x00\x00\x00\x18\x77\x6F\x72\x6C\x64\x2F\x5F\x63\x6F\x6D\x6D\x6F\x6E\x2F\x6D\x61\x74\x73\x68\x61\x64\x65\x72\x2F\xD7\xE7\xD9\xC7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3F\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'
menuartbottom6=b'\x9E\xF6\x8A\xF0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x17\x6D\x75\x6C\x74\x69\x74\x65\x78\x74\x75\x72\x65\x5F\x31\x6C\x61\x79\x65\x72\x2E\x6D\x73\x68\x00\x00\x00\x18\x77\x6F\x72\x6C\x64\x2F\x5F\x63\x6F\x6D\x6D\x6F\x6E\x2F\x6D\x61\x74\x73\x68\x61\x64\x65\x72\x2F\xD7\xE7\xD9\xC7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3F\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'

coach1act=open(codename+'/cache/itf_cooked/pc/world/maps/'+codenamelow+'/menuart/actors/'+codenamelow+'_coach_1.act.ckd','wb')
coach1act.write(coach)
coach1act.write(struct.pack(">I",len(coach1tganame))+coach1tganame.encode())
coach1act.write(struct.pack(">I",len(menuartpath))+menuartpath.encode()+struct.pack("<I",zlib.crc32(coach1tganame.encode())))
coach1act.write(menuartbottom1)
coach1act.close()

coach2act=open(codename+'/cache/itf_cooked/pc/world/maps/'+codenamelow+'/menuart/actors/'+codenamelow+'_coach_2.act.ckd','wb')
coach2act.write(coach)
coach2act.write(struct.pack(">I",len(coach2tganame))+coach2tganame.encode())
coach2act.write(struct.pack(">I",len(menuartpath))+menuartpath.encode()+struct.pack("<I",zlib.crc32(coach2tganame.encode())))
coach2act.write(menuartbottom1)
coach2act.close()

coach3act=open(codename+'/cache/itf_cooked/pc/world/maps/'+codenamelow+'/menuart/actors/'+codenamelow+'_coach_3.act.ckd','wb')
coach3act.write(coach)
coach3act.write(struct.pack(">I",len(coach3tganame))+coach3tganame.encode())
coach3act.write(struct.pack(">I",len(menuartpath))+menuartpath.encode()+struct.pack("<I",zlib.crc32(coach3tganame.encode())))
coach3act.write(menuartbottom1)
coach3act.close()

coach4act=open(codename+'/cache/itf_cooked/pc/world/maps/'+codenamelow+'/menuart/actors/'+codenamelow+'_coach_4.act.ckd','wb')
coach4act.write(coach)
coach4act.write(struct.pack(">I",len(coach4tganame))+coach4tganame.encode())
coach4act.write(struct.pack(">I",len(menuartpath))+menuartpath.encode()+struct.pack("<I",zlib.crc32(coach4tganame.encode())))
coach4act.write(menuartbottom1)
coach4act.close()

albumcoachact=open(codename+'/cache/itf_cooked/pc/world/maps/'+codenamelow+'/menuart/actors/'+codenamelow+'_cover_albumcoach.act.ckd','wb')
albumcoachact.write(coach)
albumcoachact.write(struct.pack(">I",len(albumcoachtganame))+albumcoachtganame.encode())
albumcoachact.write(struct.pack(">I",len(menuartpath))+menuartpath.encode()+struct.pack("<I",zlib.crc32(albumcoachtganame.encode())))
albumcoachact.write(menuartbottom1)
albumcoachact.close()

albumbkgact=open(codename+'/cache/itf_cooked/pc/world/maps/'+codenamelow+'/menuart/actors/'+codenamelow+'_cover_albumbkg.act.ckd','wb')
albumbkgact.write(coach)
albumbkgact.write(struct.pack(">I",len(albumbkgtganame))+albumbkgtganame.encode())
albumbkgact.write(struct.pack(">I",len(menuartpath))+menuartpath.encode()+struct.pack("<I",zlib.crc32(albumbkgtganame.encode())))
albumbkgact.write(menuartbottom1)
albumbkgact.close()

genericact=open(codename+'/cache/itf_cooked/pc/world/maps/'+codenamelow+'/menuart/actors/'+codenamelow+'_cover_generic.act.ckd','wb')
genericact.write(coach)
genericact.write(struct.pack(">I",len(generictganame))+generictganame.encode())
genericact.write(struct.pack(">I",len(menuartpath))+menuartpath.encode()+struct.pack("<I",zlib.crc32(generictganame.encode())))
genericact.write(menuartbottom1)
genericact.close()

onlineact=open(codename+'/cache/itf_cooked/pc/world/maps/'+codenamelow+'/menuart/actors/'+codenamelow+'_cover_online.act.ckd','wb')
onlineact.write(coach)
onlineact.write(struct.pack(">I",len(onlinetganame))+onlinetganame.encode())
onlineact.write(struct.pack(">I",len(menuartpath))+menuartpath.encode()+struct.pack("<I",zlib.crc32(onlinetganame.encode())))
onlineact.write(menuartbottom1)
onlineact.close()

banact=open(codename+'/cache/itf_cooked/pc/world/maps/'+codenamelow+'/menuart/actors/'+codenamelow+'_banner_bkg.act.ckd','wb')
banact.write(coach)
banact.write(struct.pack(">I",len(bannertganame))+bannertganame.encode())
banact.write(struct.pack(">I",len(menuartpath))+menuartpath.encode()+struct.pack("<I",zlib.crc32(bannertganame.encode())))
banact.write(menuartbottom1)
banact.close()

menuartiscsuper='<?xml version="1.0" encoding="ISO-8859-1"?><root><Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="1"><ACTORS NAME="Actor"><Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="'+codename+'_cover_generic" MARKER="" POS2D="266.087555 197.629959" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl"><COMPONENTS NAME="MaterialGraphicComponent"><MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000"><PrimitiveParameters><GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000"><ENUM NAME="gfxOccludeInfo" SEL="0" /></GFXPrimitiveParam></PrimitiveParameters><ENUM NAME="anchor" SEL="1" /><material><GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295"><textureSet><GFXMaterialTexturePathSet diffuse="world/maps/'+codenamelow+'/menuart/textures/'+codenamelow+'_cover_generic.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" /></textureSet><materialParams><GFXMaterialSerializableParam Reflector_factor="0.000000" /></materialParams></GFXMaterialSerializable></material><ENUM NAME="oldAnchor" SEL="1" /></MaterialGraphicComponent></COMPONENTS></Actor></ACTORS><ACTORS NAME="Actor"><Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="'+codename+'_cover_online" MARKER="" POS2D="-150.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl"><COMPONENTS NAME="MaterialGraphicComponent"><MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000"><PrimitiveParameters><GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000"><ENUM NAME="gfxOccludeInfo" SEL="0" /></GFXPrimitiveParam></PrimitiveParameters><ENUM NAME="anchor" SEL="1" /><material><GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295"><textureSet><GFXMaterialTexturePathSet diffuse="world/maps/'+codenamelow+'/menuart/textures/'+codenamelow+'_cover_online.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" /></textureSet><materialParams><GFXMaterialSerializableParam Reflector_factor="0.000000" /></materialParams></GFXMaterialSerializable></material><ENUM NAME="oldAnchor" SEL="1" /></MaterialGraphicComponent></COMPONENTS></Actor></ACTORS><ACTORS NAME="Actor"><Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="'+codename+'_cover_albumcoach" MARKER="" POS2D="738.106323 359.612030" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl"><COMPONENTS NAME="MaterialGraphicComponent"><MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000"><PrimitiveParameters><GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000"><ENUM NAME="gfxOccludeInfo" SEL="0" /></GFXPrimitiveParam></PrimitiveParameters><ENUM NAME="anchor" SEL="6" /><material><GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295"><textureSet><GFXMaterialTexturePathSet diffuse="world/maps/'+codenamelow+'/menuart/textures/'+codenamelow+'_cover_albumcoach.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" /></textureSet><materialParams><GFXMaterialSerializableParam Reflector_factor="0.000000" /></materialParams></GFXMaterialSerializable></material><ENUM NAME="oldAnchor" SEL="6" /></MaterialGraphicComponent></COMPONENTS></Actor></ACTORS><ACTORS NAME="Actor"><Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="'+codename+'_cover_albumbkg" MARKER="" POS2D="1067.972168 201.986328" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl"><COMPONENTS NAME="MaterialGraphicComponent"><MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000"><PrimitiveParameters><GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000"><ENUM NAME="gfxOccludeInfo" SEL="0" /></GFXPrimitiveParam></PrimitiveParameters><ENUM NAME="anchor" SEL="1" /><material><GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295"><textureSet><GFXMaterialTexturePathSet diffuse="world/maps/'+codenamelow+'/menuart/textures/'+codenamelow+'_cover_albumbkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" /></textureSet><materialParams><GFXMaterialSerializableParam Reflector_factor="0.000000" /></materialParams></GFXMaterialSerializable></material><ENUM NAME="oldAnchor" SEL="1" /></MaterialGraphicComponent></COMPONENTS></Actor></ACTORS><ACTORS NAME="Actor"><Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="'+codename+'_coach_1" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl"><COMPONENTS NAME="MaterialGraphicComponent"><MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000"><PrimitiveParameters><GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000"><ENUM NAME="gfxOccludeInfo" SEL="0" /></GFXPrimitiveParam></PrimitiveParameters><ENUM NAME="anchor" SEL="6" /><material><GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295"><textureSet><GFXMaterialTexturePathSet diffuse="world/maps/'+codenamelow+'/menuart/textures/'+codenamelow+'_coach_1.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" /></textureSet><materialParams><GFXMaterialSerializableParam Reflector_factor="0.000000" /></materialParams></GFXMaterialSerializable></material><ENUM NAME="oldAnchor" SEL="6" /></MaterialGraphicComponent></COMPONENTS></Actor></ACTORS><ACTORS NAME="Actor"><Actor RELATIVEZ="0.000000" SCALE="256.000000 128.000000" xFLIPPED="0" USERFRIENDLY="'+codename+'_banner_bkg" MARKER="" POS2D="1487.410156 -32.732918" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl"><COMPONENTS NAME="MaterialGraphicComponent"><MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000"><PrimitiveParameters><GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000"><ENUM NAME="gfxOccludeInfo" SEL="0" /></GFXPrimitiveParam></PrimitiveParameters><ENUM NAME="anchor" SEL="1" /><material><GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295"><textureSet><GFXMaterialTexturePathSet diffuse="world/maps/'+codenamelow+'/menuart/textures/'+codenamelow+'_banner_bkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" /></textureSet><materialParams><GFXMaterialSerializableParam Reflector_factor="0.000000" /></materialParams></GFXMaterialSerializable></material><ENUM NAME="oldAnchor" SEL="1" /></MaterialGraphicComponent></COMPONENTS></Actor></ACTORS><sceneConfigs><SceneConfigs activeSceneConfig="0" /></sceneConfigs></Scene></root>'
menuartisc=open(codename+'/cache/itf_cooked/pc/world/maps/'+codenamelow+'/menuart/'+codenamelow+'_menuart.isc.ckd','w')
menuartisc.write(menuartiscsuper)
menuartisc.close()