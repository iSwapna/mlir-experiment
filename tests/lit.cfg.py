import os

import lit.formats
import lit.util
from lit.llvm import llvm_config
from lit.llvm.subst import FindTool, ToolSubst

#Configuration file for the 'lit' test runner.

# name: The name of the test suite
config.name = 'MLIR-EXPERIMENT'
config.test_format = lit.formats.ShTest(not llvm_config.use_lit_shell)

config.suffixes = ['.mlir']
config.test_source_root = os.path.dirname(__file__)
config.test_exec_root = os.path.join(config.triton_obj_root, 'tests')

config.substitutions.append(('%PATH%', config.environment['PATH']))
config.substitutions.append(('%shlibext', config.llvm_shlib_ext))

llvm_config.with_system_environment(
    ['HOME', 'INCLUDE', 'LIB', 'TMP', 'TEMP'])

llvm_config.use_default_substitutions()

config.excludes = ["Inputs", "Examples", "CMakeLists.txt", "README.md", "LICENSE"]
# Tweak the PATH to include the tools dir.
llvm_config.with_environment("PATH", config.llvm_tools_dir, append_path=True)
tool_dirs = [config.llvm_tools_dir]
tools = ["mlir-opt",]

llvm_config.add_tool_substitutions(tools, tool_dirs)
