<?php

class Gallery_model extends CI_Model {

    var $gallery_path;
    var $gallery_path_url;

    function __construct() {
        parent::__construct();

        $this->gallery_path = realpath(APPPATH . '../images');
        $this->gallery_path_url = base_url() . 'images/';
    }

    function do_upload() {

        $this->load->library('upload');
        $this->upload->do_upload();
        $image_data = $this->upload->data();

        $config = array(
            'source_image' => $image_data['full_path'],
            'new_image' => $this->gallery_path . '/thumbs',
            'maintain_ratio' => true,
            'width' => 150,
            'height' => 100
        );

        $this->load->library('image_lib', $config);
        $this->image_lib->resize();
    }

    function get_images() {

        $files = scandir($this->gallery_path);
        $files = array_diff($files, array('.', '..', 'thumbs'));

        $images = array();

        foreach ($files as $file) {
            $images [] = array(
                'url' => $this->gallery_path_url . $file,
                'thumb_url' => $this->gallery_path_url . 'thumbs/' . $file
            );
        }

        return $images;
    }

}

