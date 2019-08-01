#!/bin/ksh


mkres()
{

    MKSYSB_FLAGS=
    COMMENTS=
    MK_IMAGE=
    SERVER=
    EXCLUDE_FILES=
    SOURCE=
    LOCATION=
    while getopts N:s:l:c:mS:fT option
    do
        case $option in 
            N) NAME=$OPTARG ;;
            s) SERVER=-aserver=$OPTARG ;;
            l) LOCATION=-alocation=$OPTARG ;;
            c) COMMENTS="$OPTARG" ;;
            m) MK_IMAGE=-amk_image=yes ;;
            S) SOURCE=-asource=$OPTARG ;;
            f) MKSYSB_FLAGS=${MKSYSB_FLAGS}e ;;
            T) MKSYSB_FLAGS=${MKSYSB_FLAGS}T ;;
        esac
    done
}
#                                                                               |       nim -o define -t ${TYPE} ${FORCE} ${SERVER} ${LOCATION} ${SOURCE}  |                                                                                
#                                                                               |           ${MK_IMAGE} ${MKSYSB_FLAGS:+-amksysb_flags=$MKSYSB_FLAGS}      |                                                                                
#                                                                               |           ${NFS_SEC:+-a nfs_sec=$NFS_SEC} ${NFS_VERS:+-a nfs_vers=$NFS_V |                                                                                
#                                                                               |   ERS}         ${EXCLUDE_FILES} ${SIZE_PREVIEW}                          |                                                                                
#                                                                               |                ${REP_SRC:+-a source=$REP_SRC}                            |                                                                                
#                                                                               |                ${COMMENTS:+-acomments="${COMMENTS}"} ${NAME}             |                                                                                
#                                                                               |       exit $?                                                            |                                                                                
#                                                                               |   }                                                                      |                                                                                
#                                                                               |   mkres -N 's-advstg-01-nfs3206_mk_2019_0801_Thu' -t 'mksysb' -s 'netapp |                                                                                
#                                                                               |   _8040' -l '/vol_advnim_mksysb/s-advstg-01-nfs3206_mk_2019_0801_Thu' '- |                                                                                
#                                                                               |   m' -S's-advstg-01-nfs3206'  -f'e' '-T' '-A'                            |                                                                                
#                                                                               | [BOTTOM]                                                                 |                                                                                
#                                                                               |                                                                          |                                                                                
#F1=Help                                                   F2=Refresh           | F1=Help                 F2=Refresh              F3=Cancel                |                     F4=List                                                    
#F5=Reset                                                  F6=Command           | F8=Image                F10=Exit                Enter=Do                 |                     F8=Image                                                   
#F9=Shell                                                  F10=Exit             +--------------------------------------------------------------------------+                                                                                
#
#
#---------- end of screen ----------
#
#
#[Aug 01 2019, 00:13:28]
#    Exiting SMIT
#
