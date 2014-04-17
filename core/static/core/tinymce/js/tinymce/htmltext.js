var tiny_config = {
    selector: "textarea.htmltext",
    theme: "modern",
    menubar:false,
    plugins: [
         "advlist autolink link image lists charmap preview hr anchor pagebreak spellchecker",
         "searchreplace visualblocks visualchars fullscreen insertdatetime media nonbreaking",
         "save table contextmenu directionality template paste textcolor code"
   ],
   toolbar: "undo redo | bold italic underline | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image media | code"

}

tinymce.init(tiny_config);
django.jQuery(function(){
   django.jQuery('.add-row a').click(function(){
        tinymce.init(tiny_config);
   });
});