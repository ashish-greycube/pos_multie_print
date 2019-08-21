// https://erpnext.com/docs/user/manual/en/setting-up/print/raw-printing
frappe.ui.form.on("ToDo", {
	validate: function(frm) {
        console.log('validate')
        // frm.print_preview.get_print_format()
       let  me=frm.print_preview
       let selected_format=frm.print_preview.print_formats[1]
       frm.meta.default_print_format=selected_format
       console.log('validate',me.is_raw_printing(selected_format))
    

        if (me.is_raw_printing(selected_format)) {
            console.log('1')
            frappe.call({
                method: "frappe.www.printview.get_rendered_raw_commands",
                args: {
                    doc: frm.doc,
                    print_format: selected_format,
                    _lang: 'en'
                },
                callback: function (r) {
                    if (!r.exc) {
                        // callback(r.message);
                        let out=r.message;
                        console.log('out',out)



                        frappe.ui.form.qz_connect().then(function () {

                            let printer_map = me.get_mapped_printer()[0];
                            console.log(printer_map)
                            printer_map = {idx: 1, __islocal: true, print_format: "MutliPrint", printer: "zebra"}
                            let data = [out.raw_commands];
                            let config = qz.configs.create(printer_map.printer);
                            console.log('printer_map','data','config')
                            console.log(printer_map,data,config)
                            return qz.print(config, data);
                        }).then(frappe.ui.form.qz_success).catch((err) => {
                            frappe.ui.form.qz_fail(err);
                        });
                    }
                }
            });





    }
}
});
