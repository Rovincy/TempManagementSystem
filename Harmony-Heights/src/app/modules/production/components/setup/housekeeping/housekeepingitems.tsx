import {Button, Form, Input, InputNumber, Modal, Space, Table, message} from 'antd'
import {useEffect, useState} from 'react'
import axios from 'axios'
import {KTCardBody, KTSVG} from '../../../../../../_metronic/helpers'
import {BASE_URL} from '../../../urls'
import {Link, useParams} from 'react-router-dom'
// import { employeedata } from '../../../../../data/DummyData'
import {QueryClient, useMutation, useQuery, useQueryClient} from 'react-query'
import {
  Api_Endpoint,
  addCategoryServiceApi,
  addHouseItemApi,
  fetchHouseKeepingApi,
  fetchRooms,
  fetchServiceDetailsApi,
} from '../../../../../services/ApiCalls'
import Checkbox from 'antd/es/checkbox/Checkbox'
import TextArea from 'antd/es/input/TextArea'

const Housekeepingitems = () => {
  const [loading, setLoading] = useState(false)
  const [searchText, setSearchText] = useState('')

  const [submitLoading, setSubmitLoading] = useState(false)
  const [form] = Form.useForm()
  const [img, setImg] = useState()
  const queryClient = useQueryClient()

  const {data: HouseKeepingData} = useQuery('fetchItems', fetchHouseKeepingApi)
  const {mutate: addHouseItemData} = useMutation((values: any) => addHouseItemApi(values))
  const [openNoteModal, setopenNoteModal] = useState(false)
  const parms: any = useParams()
  const [categoryForm] = Form.useForm()
  const cancelNoteModal = () => {
    setopenNoteModal(false)
  }
  const data = HouseKeepingData?.data.filter((item: any) => {
    return item.serviceCategoryId == parms.id
  })
  const submitService = (values: any) => {
    values.serviceCategoryId = parms.id
    Modal.confirm({
      okText: 'Ok',
      okType: 'primary',
      title: 'Are you sure, you want to add this item?',
      onOk: () => {
        addHouseItemData(values, {
          onSuccess: () => {
            message.info('Item added successfully!')
            queryClient.invalidateQueries('fetchItems')
            setopenNoteModal(false)
            categoryForm.resetFields()
          },
        })
      },
    })
  }
  const deleteData = async (element: any) => {
    Modal.confirm({
    okText: 'Yes',
    okType: 'primary',
    title: 'Are you sure, you want to delete this item',
    onOk: async () => {
        const response = await axios.delete(`${BASE_URL}/HouseKeeping/${element}`)
    // update the local state so that react can refecth and re-render the table with the new data
    // const newData = gridData.filter((item: any) => item.id !== element.id)
    // setGridData(newData)
    if (response.status==200) {
      message.success("Item deleted successfully")
      queryClient.invalidateQueries('fetchItems')
    }else{
      message.success("Item deletion failed")
    }
    return response.status
    },
  })
}
  const addHouseItems = () => {
    setopenNoteModal(true)
  }
  const columns: any = [
    {
      title: 'Item',
      dataIndex: 'name',
      sorter: (a: any, b: any) => {
        if (a.name > b.name) {
          return 1
        }
        if (b.name > a.name) {
          return -1
        }
        return 0
      },
    },
    {
      title: 'Description',
      dataIndex: 'description',
      sorter: (a: any, b: any) => {
        if (a.name > b.name) {
          return 1
        }
        if (b.name > a.name) {
          return -1
        }
        return 0
      },
    },
    {
      title: 'Quantity',
      dataIndex: 'quantity',
      sorter: (a: any, b: any) => {
        if (a.name > b.name) {
          return 1
        }
        if (b.name > a.name) {
          return -1
        }
        return 0
      },
    },

    {
      title: 'Action',
      fixed: 'right',
      width: 20,
      render: (_: any, record: any) => (
        <Space size='middle'>
          {/* <Link to={`/employee-edit-form/${record.id}`}>
          <span className='btn btn-light-info btn-sm delete-button' style={{ backgroundColor: 'blue', color: 'white' }}>Rooms</span>
          </Link> */}
          <Link to={""}/*to={`/employee-edit-form/${record.id}`}*/>
            <span
              className='btn btn-light-info btn-sm delete-button'
              style={{backgroundColor: 'red', color: 'white'}}
              onClick={()=>deleteData(record.id)}
            >
              Delete
            </span>
          </Link>
        </Space>
      ),
    },
  ]

  const globalSearch = () => {
    // @ts-ignore
    filteredData = dataWithIndex.filter((value) => {
      return (
        value.name.toLowerCase().includes(searchText.toLowerCase()) ||
        value.description.toLowerCase().includes(searchText.toLowerCase()) ||
        value.price.toLowerCase().includes(searchText.toLowerCase())
      )
    })
  }

  return (
    // <div
    //   style={{
    //     backgroundColor: 'white',
    //     padding: '20px',
    //     borderRadius: '5px',
    //     boxShadow: '2px 2px 15px rgba(0,0,0,0.08)',
    //   }}
    // >
    <div
      style={{
        width: '100%',
        backgroundColor: 'white',
        padding: '20px',
        borderRadius: '5px',
        boxShadow: '2px 2px 15px rgba(0,0,0,0.08)',
      }}
    >
      <KTCardBody className='py-4 '>
        <div className='table-responsive'>
          <Link to='/housekeeping'>
            <a
              style={{fontSize: '16px', fontWeight: '500'}}
              className='mb-7 btn btn-outline btn-outline-dashed btn-outline-primary btn-active-light-primary'
            >
              Back to service category
            </a>
          </Link>
          <div className='d-flex justify-content-between'>
            <Space style={{marginBottom: 16}}>
              <Input placeholder='Enter Search Text' type='text' allowClear value={searchText} />
              <Button type='primary' onClick={globalSearch}>
                Search
              </Button>
            </Space>
            <Space style={{marginBottom: 16}}>
              <button
                type='button'
                className='btn btn-primary me-3'
                onClick={() => addHouseItems()}
              >
                <KTSVG path='/media/icons/duotune/arrows/arr075.svg' className='svg-icon-2' />
                Add
              </button>

              <button type='button' className='btn btn-light-primary me-3'>
                <KTSVG path='/media/icons/duotune/arrows/arr078.svg' className='svg-icon-2' />
                Export
              </button>
            </Space>
          </div>
          <Table columns={columns} className='table-responsive' dataSource={data} />
        </div>
        <Modal
          open={openNoteModal}
          okText='Ok'
          title='Add Service '
          closable={true}
          onCancel={cancelNoteModal}
          footer={null}
        >
          <Form form={categoryForm} onFinish={submitService}>
            <Form.Item
              name={'name'}
              label='Item'
              rules={[{required: true, message: 'Please enter item'}]}
              hasFeedback
              style={{width: '100%'}}
              labelCol={{span: 5}}
            >
              <Input type='text' style={{width: '100%'}} />
            </Form.Item>
            <Form.Item
              name={'quantity'}
              label='Quantity'
              rules={[{required: true, message: 'Please enter quantity'}]}
              hasFeedback
              style={{width: '100%'}}
              labelCol={{span: 5}}
            >
              <Input type='number' style={{width: '100%'}} />
            </Form.Item>
            <Form.Item
              label='Description'
              rules={[{required: true, message: 'Please enter description'}]}
              name={'description'}
              hasFeedback
              style={{width: '100%'}}
              labelCol={{span: 5}}
            >
              <TextArea rows={4} style={{width: '100%'}} />
            </Form.Item>

            <Form.Item wrapperCol={{offset: 5, span: 18}}>
              <Button type='primary' key='submit' htmlType='submit'>
                Submit
              </Button>
            </Form.Item>
          </Form>
        </Modal>
      </KTCardBody>
    </div>
  )
}

export {Housekeepingitems}
