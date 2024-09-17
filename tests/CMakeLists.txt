
llvm_canonicalize_cmake_booleans(
  MLIR_ENABLE_BINDINGS_PYTHON
)

configure_lit_site_cfg(
    ${CMAKE_CURRENT_SOURCE_DIR}/lit.site.cfg.py.in
    ${CMAKE_CURRENT_SOURCE_DIR}/lit.site.cfg.py
    MAIN_CONFIG 
    ${CMAKE_CURRENT_SOURCE_DIR}/lit.cfg.py
)

set (MLIR_TUTORIAL_TEST_DEPENDS
    FileCheck
    mlir-opt
)

set(FILECHECK_PATH "${LLVM_LIBRARY_DIR}/../bin/FileCheck")
message("llvm dir: ${FILECHECK_PATH}")
set(LIT_ARGS "-Dfilecheck=${FILECHECK_PATH}")


add_lit_testsuite(check-mlir-tutorial "Running mlir-exp tests"
    ${CMAKE_CURRENT_SOURCE_DIR}
    DEPENDS ${MLIR_TUTORIAL_TEST_DEPENDS}
)
