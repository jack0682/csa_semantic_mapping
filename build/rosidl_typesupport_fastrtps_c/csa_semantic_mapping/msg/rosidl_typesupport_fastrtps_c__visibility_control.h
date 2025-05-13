// generated from
// rosidl_typesupport_fastrtps_c/resource/rosidl_typesupport_fastrtps_c__visibility_control.h.in
// generated code does not contain a copyright notice

#ifndef CSA_SEMANTIC_MAPPING__MSG__ROSIDL_TYPESUPPORT_FASTRTPS_C__VISIBILITY_CONTROL_H_
#define CSA_SEMANTIC_MAPPING__MSG__ROSIDL_TYPESUPPORT_FASTRTPS_C__VISIBILITY_CONTROL_H_

#if __cplusplus
extern "C"
{
#endif

// This logic was borrowed (then namespaced) from the examples on the gcc wiki:
//     https://gcc.gnu.org/wiki/Visibility

#if defined _WIN32 || defined __CYGWIN__
  #ifdef __GNUC__
    #define ROSIDL_TYPESUPPORT_FASTRTPS_C_EXPORT_csa_semantic_mapping __attribute__ ((dllexport))
    #define ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_csa_semantic_mapping __attribute__ ((dllimport))
  #else
    #define ROSIDL_TYPESUPPORT_FASTRTPS_C_EXPORT_csa_semantic_mapping __declspec(dllexport)
    #define ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_csa_semantic_mapping __declspec(dllimport)
  #endif
  #ifdef ROSIDL_TYPESUPPORT_FASTRTPS_C_BUILDING_DLL_csa_semantic_mapping
    #define ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_csa_semantic_mapping ROSIDL_TYPESUPPORT_FASTRTPS_C_EXPORT_csa_semantic_mapping
  #else
    #define ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_csa_semantic_mapping ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_csa_semantic_mapping
  #endif
#else
  #define ROSIDL_TYPESUPPORT_FASTRTPS_C_EXPORT_csa_semantic_mapping __attribute__ ((visibility("default")))
  #define ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_csa_semantic_mapping
  #if __GNUC__ >= 4
    #define ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_csa_semantic_mapping __attribute__ ((visibility("default")))
  #else
    #define ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_csa_semantic_mapping
  #endif
#endif

#if __cplusplus
}
#endif

#endif  // CSA_SEMANTIC_MAPPING__MSG__ROSIDL_TYPESUPPORT_FASTRTPS_C__VISIBILITY_CONTROL_H_
