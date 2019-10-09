
(cl:in-package :asdf)

(defsystem "scan-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "LidarDatas" :depends-on ("_package_LidarDatas"))
    (:file "_package_LidarDatas" :depends-on ("_package"))
  ))