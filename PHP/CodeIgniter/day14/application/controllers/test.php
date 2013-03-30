<?php

class Test extends CI_Controller {

    function allowed_chars($param) {

        echo "You passed me $param";
    }

    function md5_test($pass) {

        echo md5($pass);
    }

    function sha1_test($pass) {

        echo sha1($pass);
    }

    function sha1_test2($pass) {

        $this->load->library('encrypt');

        echo $this->encrypt->sha1($pass);
    }

    function encode() {

        $message = 'This is a secret message.';
        $this->load->library('encrypt');

        echo $this->encrypt->encode($message);
    }

    function decode() {

        $this->load->library('encrypt');

        $encrypted_message = 'GNUV8k/c9TM8NiVOxNd0dmyTxKA4Mt+At2R3iu2rEcXLCyXMgA3HER7MMpXK9HVsjU3NzG44kEOekIkhj7N4YA==';

        echo $this->encrypt->decode($encrypted_message);
    }

    function encode_with_key($key) {

        $message = 'This is a secret message.';
        $this->load->library('encrypt');

        echo $this->encrypt->encode($message, $key);
    }

    function decode_with_key($key) {

        $this->load->library('encrypt');

        $encrypted_message = 'S/YwKs4Wbiq/TysrHnBz8dBR/CErCDxEwnxI1j5pAzUnqrCTTbqNRN/6LA8c+nefdhivsgGkzXM9UukczOaZ+A==';

        echo $this->encrypt->decode($encrypted_message, $key);
    }

    function sql() {

        $name = 'Jubic';

        // Unsafe
        $query = "SELECT * FROM `users` WHERE `name` = `$name`";

        $query = "SELECT * FROM `users` WHERE `name` = '" . mysqli_real_escape_string($name) . "'";

        $query = "SELECT * FROM `users` WHERE `name` = '".$this->db->escape_str($name)."'";

        $query = "SELECT * FROM `users` WHERE `name` = ".$this->db->escape($name)."";

        $query = "SELECT * FROM `users` WHERE `name` LIKE '%".$this->db->escape($name)."%'";

        // No escaping needed when using Active Records.
        $this->db->select('*')->from('users')->where('name', $name);
    }

    function xss_filter() {

        // Filtered by config
        $this->input->post('comment', true);

        // XSS
        $this->input->post('comment', true);

        $this->input->xss_clean($string);

    }

    function output() {

        htmlspecialchars($string);

        // Automatically filtered
        echo anchor($url);

        // Automatically filtered
        echo form_input('name', set_value('name'));

        ?>
<input type="text" name="name" value="<?php if(isset($_POST['name'])) echo htmlspecialchars($_POST['name']);?>">
<?php
    }

    function session() {

        $this->load->library('session');

        $this->session->set_userdata('user_id', 2);

    }

    function session_read() {

        $this->load->library('session');

        $user_id = $this->session->userdata('user_id');

        if ($user_id == 1) {

            echo "You have all access. User id: $user_id";

        }

        else {

            echo "You have limited access user. User id: $user_id";

        }

    }

    function error() {

        foobar();

    }

    function _secret() {

        echo 'You\'ve called secret';
    }

}

?>