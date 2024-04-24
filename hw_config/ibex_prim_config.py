
ibex_prim = {
    "config_name": "ibex_prim",

    "rtl_files": [
        "dv/uvm/core_ibex/common/prim/prim_pkg.sv",
        "vendor/lowrisc_ip/ip/prim/rtl/prim_cipher_pkg.sv",
        "vendor/lowrisc_ip/ip/prim/rtl/prim_ram_1p_pkg.sv",
        "vendor/lowrisc_ip/ip/prim/rtl/prim_mubi_pkg.sv",
        "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_pkg.sv",
        "syn/rtl/prim_clock_gating.v",
        "dv/uvm/core_ibex/common/prim/prim_ram_1p.sv",
        "dv/uvm/core_ibex/common/prim/prim_buf.sv",
        # "dv/uvm/core_ibex/common/prim/prim_clock_mux2.sv",
        "vendor/lowrisc_ip/ip/prim_generic/rtl/prim_generic_buf.sv",
        # "dv/uvm/core_ibex/common/prim/prim_flop.sv",
        "vendor/lowrisc_ip/ip/prim/rtl/prim_assert.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_util_pkg.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_pkg.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_22_16_dec.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_22_16_enc.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_64_57_dec.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_64_57_enc.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_hamming_22_16_dec.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_hamming_22_16_enc.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_hamming_39_32_dec.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_hamming_39_32_enc.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_hamming_72_64_dec.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_hamming_72_64_enc.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_ram_1p_pkg.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_ram_1p_adv.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_ram_1p_scr.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_cipher_pkg.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_lfsr.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_inv_28_22_enc.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_inv_28_22_dec.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_inv_39_32_enc.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_inv_39_32_dec.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_inv_72_64_enc.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_inv_72_64_dec.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_prince.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_subst_perm.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_28_22_enc.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_28_22_dec.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_39_32_enc.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_39_32_dec.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_72_64_enc.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_72_64_dec.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_onehot_check.sv",
        # "vendor/lowrisc_ip/ip/prim/rtl/prim_mubi_pkg.sv",
        # "vendor/lowrisc_ip/ip/prim_generic/rtl/prim_generic_ram_1p.sv",
        # "vendor/lowrisc_ip/ip/prim_generic/rtl/prim_generic_clock_gating.sv",
        # "vendor/lowrisc_ip/ip/prim_generic/rtl/prim_generic_clock_mux2.sv",
        # "vendor/lowrisc_ip/ip/prim_generic/rtl/prim_generic_flop.sv",

    ],

    "rtl_incdirs": [
        "vendor/lowrisc_ip/ip/prim/rtl/",
        "vendor/lowrisc_ip/dv/sv/dv_utils/"
    ],

    "rtl_dependencies": [],

    "tb_files": [
    ],

    "tb_incdirs": [],

    "tb_dependencies": [


    ],

    "verilog_wrapper": "",
}
