<?php
$gallery_path = realpath(APPPATH . '../images');

$config['allowed_types'] = 'jpg|jpeg|gif|png';
$config['upload_path'] = $gallery_path;
$config['max_size'] = 2000;
$config['remove_spaces'] = true;

?>