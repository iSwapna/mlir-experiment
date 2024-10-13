
Experiment with mlir

### build & test

This project links against the locally installed llvm using `llvm-config`. Since we are using an installed version of llvm (as oppsed to building from source), we need to set the path to the `lit` tool from LLVM. For this, set the LLVM_EXTERNAL_LIT cmake argument either to the install directory of llvm-project or the one in your pyenv.
```
pip install lit

cmake ../mlir-experiment -G Ninja -DLLVM_EXTERNAL_LIT=<path/to/lit>

ninja check-mlir-tutorial
```

