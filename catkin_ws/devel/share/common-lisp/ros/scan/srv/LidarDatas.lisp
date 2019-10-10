; Auto-generated. Do not edit!


(cl:in-package scan-srv)


;//! \htmlinclude LidarDatas-request.msg.html

(cl:defclass <LidarDatas-request> (roslisp-msg-protocol:ros-message)
  ((scanDataRequest
    :reader scanDataRequest
    :initarg :scanDataRequest
    :type cl:string
    :initform ""))
)

(cl:defclass LidarDatas-request (<LidarDatas-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LidarDatas-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LidarDatas-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name scan-srv:<LidarDatas-request> is deprecated: use scan-srv:LidarDatas-request instead.")))

(cl:ensure-generic-function 'scanDataRequest-val :lambda-list '(m))
(cl:defmethod scanDataRequest-val ((m <LidarDatas-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader scan-srv:scanDataRequest-val is deprecated.  Use scan-srv:scanDataRequest instead.")
  (scanDataRequest m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LidarDatas-request>) ostream)
  "Serializes a message object of type '<LidarDatas-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'scanDataRequest))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'scanDataRequest))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LidarDatas-request>) istream)
  "Deserializes a message object of type '<LidarDatas-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'scanDataRequest) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'scanDataRequest) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LidarDatas-request>)))
  "Returns string type for a service object of type '<LidarDatas-request>"
  "scan/LidarDatasRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LidarDatas-request)))
  "Returns string type for a service object of type 'LidarDatas-request"
  "scan/LidarDatasRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LidarDatas-request>)))
  "Returns md5sum for a message object of type '<LidarDatas-request>"
  "b24f18b58a2ea88af3a36911a1be8ff0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LidarDatas-request)))
  "Returns md5sum for a message object of type 'LidarDatas-request"
  "b24f18b58a2ea88af3a36911a1be8ff0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LidarDatas-request>)))
  "Returns full string definition for message of type '<LidarDatas-request>"
  (cl:format cl:nil "string scanDataRequest~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LidarDatas-request)))
  "Returns full string definition for message of type 'LidarDatas-request"
  (cl:format cl:nil "string scanDataRequest~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LidarDatas-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'scanDataRequest))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LidarDatas-request>))
  "Converts a ROS message object to a list"
  (cl:list 'LidarDatas-request
    (cl:cons ':scanDataRequest (scanDataRequest msg))
))
;//! \htmlinclude LidarDatas-response.msg.html

(cl:defclass <LidarDatas-response> (roslisp-msg-protocol:ros-message)
  ((scanDataResponse
    :reader scanDataResponse
    :initarg :scanDataResponse
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (scanDataHand
    :reader scanDataHand
    :initarg :scanDataHand
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass LidarDatas-response (<LidarDatas-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LidarDatas-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LidarDatas-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name scan-srv:<LidarDatas-response> is deprecated: use scan-srv:LidarDatas-response instead.")))

(cl:ensure-generic-function 'scanDataResponse-val :lambda-list '(m))
(cl:defmethod scanDataResponse-val ((m <LidarDatas-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader scan-srv:scanDataResponse-val is deprecated.  Use scan-srv:scanDataResponse instead.")
  (scanDataResponse m))

(cl:ensure-generic-function 'scanDataHand-val :lambda-list '(m))
(cl:defmethod scanDataHand-val ((m <LidarDatas-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader scan-srv:scanDataHand-val is deprecated.  Use scan-srv:scanDataHand instead.")
  (scanDataHand m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LidarDatas-response>) ostream)
  "Serializes a message object of type '<LidarDatas-response>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'scanDataResponse))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'scanDataResponse))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'scanDataHand))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'scanDataHand))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LidarDatas-response>) istream)
  "Deserializes a message object of type '<LidarDatas-response>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'scanDataResponse) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'scanDataResponse)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'scanDataHand) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'scanDataHand)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LidarDatas-response>)))
  "Returns string type for a service object of type '<LidarDatas-response>"
  "scan/LidarDatasResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LidarDatas-response)))
  "Returns string type for a service object of type 'LidarDatas-response"
  "scan/LidarDatasResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LidarDatas-response>)))
  "Returns md5sum for a message object of type '<LidarDatas-response>"
  "b24f18b58a2ea88af3a36911a1be8ff0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LidarDatas-response)))
  "Returns md5sum for a message object of type 'LidarDatas-response"
  "b24f18b58a2ea88af3a36911a1be8ff0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LidarDatas-response>)))
  "Returns full string definition for message of type '<LidarDatas-response>"
  (cl:format cl:nil "float64[] scanDataResponse~%float64[] scanDataHand~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LidarDatas-response)))
  "Returns full string definition for message of type 'LidarDatas-response"
  (cl:format cl:nil "float64[] scanDataResponse~%float64[] scanDataHand~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LidarDatas-response>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'scanDataResponse) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'scanDataHand) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LidarDatas-response>))
  "Converts a ROS message object to a list"
  (cl:list 'LidarDatas-response
    (cl:cons ':scanDataResponse (scanDataResponse msg))
    (cl:cons ':scanDataHand (scanDataHand msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'LidarDatas)))
  'LidarDatas-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'LidarDatas)))
  'LidarDatas-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LidarDatas)))
  "Returns string type for a service object of type '<LidarDatas>"
  "scan/LidarDatas")