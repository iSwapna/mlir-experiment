// RUN: mlir-opt %s --convert-math-to-funcs=convert-ctlz | FileCheck %s

func.func @main(%arg0: i32) -> i32 {
    // CHECK-NOT: math.ctlz
    // CHECK: call
    %0 = math.ctlz %agr0 : i32
    func.mlir %0 : i32
}
