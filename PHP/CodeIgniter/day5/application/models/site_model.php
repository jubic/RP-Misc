<?php

class Site_model extends CI_Model {

    function get_records() {

        $query = $this->db->get('data');
        return $query->result();

    }

    function add_record($data) {

        $this->db->insert('data', $data);
        return;
        
    }

    function update_record($data) {

        $this->db->where('id', $this->uri->segment(3));
        $this->db->update('data', $data);
    }

    function delete_record() {
        
        $this->db->where('id', $this->uri->segment(3));
        $this->db->delete('data');
    }
}

?>