<?php

class Files extends CI_Model {

    function __construct() {
        parent::__construct();
    }

    function get($userid) {
        $query = $this->db->get_where('files', array('owner' => $userid));
        return $query->result();
    }

    function add($file) {
        $this->db->insert('files', array(
            'owner' => $this->session->userdata('userid'),
            'name' => $file));
    }

    function delete($fileid) {
        $query = $this->db->get_where('files', array('id' => $fileid));
        $result = $query->result();
        $query = $this->db->delete('files', array('id' => $fileid));
        return $result[0]->name;
    }

}