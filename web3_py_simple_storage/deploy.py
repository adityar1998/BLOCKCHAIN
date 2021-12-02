from solcx import compile_standard, install_solc
import json

install_solc("0.6.0")

with open("./web3_py_simple_storage/SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    print(simple_storage_file)

compile_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.souceMap"]}
            }
        },
    },
    solc_version="0.6.0",
)

with open("./web3_py_simple_storage/compiled_code.json", "w") as file:
    json.dump(compile_sol, file)

# get bytecode

bytecode = compile_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

# get abi
abi = compile_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

print(abi)
